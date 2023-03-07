<script lang="ts">
    import type { SimpleShot } from '$client';
    import { hexbin } from 'd3-hexbin';
    import { scaleLinear } from 'd3-scale';
    import { fade } from 'svelte/transition';
    import { cubicOut } from 'svelte/easing';

    export let shotsAgainst: Record<string, SimpleShot[]>; 
    export let width: number;
    export let height: number;

    $: customHeight = width * 0.5 * 115 / 74
    $: xScale = scaleLinear()
        .domain([0, 1])
        .range([width, 0])
    $: yScale = scaleLinear()
        .domain([0.5, 1])
        .range([customHeight, 0])

    $: allShotsAgainst = Object.values(shotsAgainst).flat();
    $: hexmap = hexbin()
        .radius(width/32)
        .extent([[0, 0], [width, customHeight]]);
    $: bins = hexmap(allShotsAgainst.map(x => [xScale(x.Y), yScale(x.X)]));
    $: {hexmap; console.log(hexmap)}
    $: colorScale = scaleLinear()
        .domain([0, Math.max(...bins.map(x => x.length))])
        .range(['transparent', 'white'])
        // .range(['yellow', 'red'])
    $: console.log('max len', Math.max(...bins.map(x => x.length)))
</script>

<g transform='translate(0 {(height - customHeight) / 2})' transition:fade="{{delay: 0, duration: 300, easing: cubicOut}}">

    <clipPath id="heatmap-clip">
        <rect 
            x=0
            y=0
            width={width}
            height={customHeight-1}
        />
    </clipPath>

    {#if bins}
        <!-- <path 
            id='hexmap'
            d={hexmap.mesh()}
            fill='transparent'
        /> -->
        <g clip-path='url(#heatmap-clip)'>
            {#each bins as hex, i}
                <path
                    id='hexmap-hex{i}'
                    d={hexmap.hexagon()}
                    transform='translate({hex.x} {hex.y})'
                    fill={colorScale(hex.length)}
                />
                <!-- <use clip-path="url(#heatmap-clip)" href="#hexmap-hex{i}" fill='pink' /> -->
            {/each}
        </g>
    {/if}
</g>