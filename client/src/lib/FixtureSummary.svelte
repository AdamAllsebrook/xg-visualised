<script lang='ts'>
    import type { Fixture, Team, FixtureTeam } from '$client';
    import { scaleLinear } from 'd3-scale';
    import { colours } from '$lib/colours';
    
    export let fixture: Fixture;
    export let teams: Map<string, Team>;

    const sideSwitch = {h: 'a', a: 'h'};
    let opponent: FixtureTeam = fixture[sideSwitch[fixture.side]];
    let opponentData = teams.get(opponent.title);
    let xGA = opponentData.xGA / opponentData.games;
    const xgMin = 0.5;
    const xgMax = 2.5;

    let el: HTMLElement;
    $: x = el ? el.getBoundingClientRect().x : 0;
    $: y = el ? el.getBoundingClientRect().y : 0;
    let width: number;
    let height: number;

    let colourScale = scaleLinear()
        .domain([xgMax, xgMin])
        .range([colours.xg + 'ff', colours.xg + '33']);
    let colour = colourScale(xGA);

    let hover = false;
</script>

<div 
    bind:this={el}
    bind:clientWidth={width}
    bind:clientHeight={height}
    class='inline-block my-1 relative highlight w-full'
    on:mouseover={() => {hover = true}}
    on:focus={() => {hover = true}}
    on:mouseout={() => hover = false}
    on:blur={() => {hover = false}}
    tabindex="-1"
    style='background: linear-gradient(90deg, {colour} 0%, {colour} {xGA/xgMax * 100}%, #00000000 {xGA/xgMax * 100}%, #00000000 100%)'
>
    <!-- <div class='absolute opacity-20 w-full bottom-0' style='background-color: {colour}; height: {Math.min(xGA/3, 1) * 100}%' /> -->
    <div class='font-normal' >
        <p>{opponent.title} ({fixture.side.toUpperCase()})</p>
    </div>
    <p class='absolute top-1 pl-2 font-normal' style='left: {xGA/xgMax * 100}%'>{(opponentData?.xGA / opponentData?.games).toFixed(2)} <span class='text-grey'>xGA per 90</span></p>
    <!-- <p>{teams.get(opponent.title).xGA}</p> -->
    {#if hover}
        <div 
            class='absolute pointer-events-none z-40 p-1 translate-y-full mt-1 whitespace-nowrap shadow-lg rounded-sm opacity-80'
            style='background-color: {colours.white}; color: {colours.black}'
        >
            <p class='font-medium border-b-[1px] border-black'>{opponentData?.title} ({fixture.side.toUpperCase()})</p>
            <p>{(opponentData?.xGA / opponentData?.games).toFixed(2)} xGA90</p>
        </div>
    {/if}
</div>
