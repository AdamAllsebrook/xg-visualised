<script lang='ts'>
    import type { Fixture, Team, FixtureTeam } from '$client';
    import { scaleLinear } from 'd3-scale';
    import { colours } from '$lib/colours';
    
    export let fixture: Fixture;
    export let teams: Map<string, Team>;

    const sideSwitch = {h: 'a', a: 'h'};
    let opponent: FixtureTeam = fixture[sideSwitch[fixture.side]];
    let xGA = teams.get(opponent.title).xGA / teams.get(opponent.title).games;

    let colourScale = scaleLinear()
        .domain([3, 0])
        .range([colours.secondary, colours.accent2]);
    let colour = colourScale(xGA);
</script>

<div class='border inline-block m-1 relative rounded'>
    <!-- <div class='absolute opacity-20 w-full bottom-0' style='background-color: {colour}; height: {Math.min(xGA/3, 1) * 100}%' /> -->
    <div class='w-2 h-full float-left border-r absolute' style='background-color: {colour}'/>
    <div class='p-1 pl-3 float-right'>
        <p>{opponent.short_title} ({fixture.side.toUpperCase()})</p>
    </div>
    <!-- <p>{teams.get(opponent.title).xGA}</p> -->
</div>
