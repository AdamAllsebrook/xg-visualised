<script>
    import AxisX from '$lib/AxisX.svelte';
    import AxisY from '$lib/AxisY.svelte';
    import team_index from '$lib/util/team_index.json';
	import { spring } from 'svelte/motion';
	import { line, curveNatural } from 'd3-shape';
    import { scaleLinear, scaleLog } from 'd3-scale';
    import { max } from 'd3-array';
	import { tick } from 'svelte';

    export let matches;
    $: matches, console.log(matches);

    let width = 400;
    let height = 300;
    const baseNMatches = 5
    let dragX = spring(0); 
    let isMouseDown = false;
    $: nMatches = baseNMatches;
    const margin = { top: 30, right: 40, left: 80, bottom: 40 };

    $: xScale = scaleLinear()
        .domain([matches.length - nMatches - $dragX, matches.length - 1 - $dragX])
        .range([0, width - margin.left - margin.right]);

    $: yScale = scaleLinear()
        .domain([0, max(matches, d => d.xG)])
        .range([height - margin.top - margin.bottom, 0]);

    $: dragScale = scaleLinear()
        .domain([0, width])
        .range([0, nMatches])

    // the path generator
	$: pathLine = line()
		.x((d, i) => xScale(i))
		.y(d => yScale(d.xG))
		// .curve(curveNatural);

    function getTeamLabel(match) {
        return (match.h_a == 'h' ? team_index[match.a_team].abbr.toLowerCase() : team_index[match.h_team].abbr.toUpperCase())
    }

    function handleMouseDown(event) {
        isMouseDown = true;
    }

    function handleMouseMove(event) {
        if (isMouseDown) {
            dragX.stiffness = 1;
            $dragX += dragScale(event.movementX);
            $dragX = Math.min(Math.max($dragX, 0), matches.length - nMatches)
        }
    }

    function handleMouseUp(event) {
        isMouseDown = false;
        dragX.stiffness = 0.2;
        $dragX = Math.round($dragX);
    }


 
</script>

<svelte:window on:mousemove={handleMouseMove} on:mouseup={handleMouseUp} />
<div class='container' bind:clientWidth={width}>
    <h5 style='margin-bottom: 0'>Expected Goals per Game</h5>
    <svg {width} {height} on:mousedown={handleMouseDown}>
        <AxisX {height} {xScale} {margin} xTicks={matches.map((d, i) => [i, getTeamLabel(d)])}/>
        <AxisY {width} {yScale} {margin} />
        <g transform='translate({margin.left}, {margin.top})'>
            {#each matches as match, i}
                <circle 
                    cx={xScale(i)}
                    cy={yScale(match.xG)}
                    r=5
                />
            {/each}
            <path 
                d={pathLine(matches)}
                stroke='#cecece22'
                stroke-width=2
                fill='none'
                stroke-linecap='round'
            />
        </g>
    </svg>
</div>