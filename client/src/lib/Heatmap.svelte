<script lang="ts">
    import { hexbin } from 'd3-hexbin';
    import { scaleLinear } from 'd3-scale';
    import { fade } from 'svelte/transition';
    import { cubicOut } from 'svelte/easing';
    import { key as dataKey, type DataManager } from './data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import { colours } from './colours';
    import { viewKey, type ViewManager } from './view/viewManager';

    export let width: number;
    export let height: number;
    export let rScale: any, tweenedX: any, tweenedY: any;
    const dataManager: Writable<DataManager> = getContext(dataKey);
    const viewManager: ViewManager = getContext(viewKey);
    const teamSelected: Writable<string | null> = viewManager.teamSelected;
    $: shotsConceded = $dataManager.opponents.teamShots;

    $: customHeight = width * 0.5 * 115 / 74
    $: xScale = scaleLinear()
        .domain([0, 1])
        .range([width, 0])
    $: yScale = scaleLinear()
        .domain([0.5, 1])
        .range([customHeight, 0])

    $: allShotsConceded = shotsConceded == null 
        ? [] 
        : $teamSelected == null 
            ? [...shotsConceded].map(([_, shots]) => shots).flat()
            : shotsConceded.get($teamSelected) || [];
    $: hexmap = hexbin()
        .radius(width/64)
        .extent([[0, 0], [width, customHeight]]);
    $: bins = hexmap(allShotsConceded.map(x => [xScale(x.Y), yScale(x.X)]));
    $: colorScale = scaleLinear()
        .domain([0, Math.max(...bins.map(x => x.length))])
        .range([colours.primary, '#777'])
    $: binsIndexed = new Map(bins.map(x => [hexKey(x.x, x.y), x.length]));

    function hexKey(x: number, y: number) {
        return `${Math.round(x)}-${Math.round(y)}`;
    }
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
        <g clip-path='url(#heatmap-clip)'>
            {#each hexmap.centers() as [x, y], i}
                <path
                    id='hexmap-hex-i'
                    d={hexmap.hexagon()}
                    transform='translate({x} {y})'
                    fill={colorScale(binsIndexed.get(hexKey(x, y))) || '#0000'}
                    style='transition: fill 300ms'
                />
            {/each}
        </g>
    {/if}
</g>
