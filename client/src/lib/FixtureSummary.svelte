<script lang='ts'>
    import type { Fixture, Team, FixtureTeam } from '$client';
    import type { Writable } from 'svelte/store';
    import { getContext } from 'svelte';
    import { scaleLinear } from 'd3-scale';
    import { colours } from '$lib/colours';
	import { type HoveredData, HoveredDataType, key as hoveredDataKey } from '$lib/hoveredData';
	import FixtureTooltip from '$lib/FixtureTooltip.svelte';
    
    export let fixture: Fixture;
    export let teams: Map<string, Team>;

    let hoveredData: Writable<HoveredData | null> = getContext(hoveredDataKey);
    const sideSwitch = {h: 'a', a: 'h'};
    let opponent: FixtureTeam = fixture[sideSwitch[fixture.side]];
    let opponentData = teams.get(opponent.title);
    let xGA = opponentData.xGA / opponentData.games;

    let el: HTMLElement;
    $: x = el ? el.getBoundingClientRect().x : 0;
    $: y = el ? el.getBoundingClientRect().y : 0;
    let width: number;

    let colourScale = scaleLinear()
        .domain([3, 0])
        .range([colours.secondary, colours.accent2]);
    let colour = colourScale(xGA);
</script>

<div 
    bind:this={el}
    bind:clientWidth={width}
    class='border inline-block m-1 relative rounded drop-shadow-lg'
    on:mouseover={() => {
        hoveredData.set({data: {opponent: opponentData, position: {x: x, y: y, width: width}}, index: -1, component: FixtureTooltip, type: HoveredDataType.Fixture}); 
    }}
    on:focus={() => {
        hoveredData.set({data: {opponent: opponentData, position: {x: x, y: y, width: width}}, index: -1, component: FixtureTooltip, type: HoveredDataType.Fixture}); 
    }}
    on:mouseout={() => hoveredData.set(null)}
    on:blur={() => hoveredData.set(null)}
>
    <!-- <div class='absolute opacity-20 w-full bottom-0' style='background-color: {colour}; height: {Math.min(xGA/3, 1) * 100}%' /> -->
    <div class='w-2 h-full float-left border-r absolute' style='background-color: {colour}'/>
    <div class='p-1 pl-3 float-right'>
        <p>{opponent.short_title} ({fixture.side.toUpperCase()})</p>
    </div>
    <!-- <p>{teams.get(opponent.title).xGA}</p> -->
</div>
