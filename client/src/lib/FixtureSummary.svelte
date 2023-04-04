<script lang='ts'>
    import type { Team } from '$client';
    import { scaleLinear } from 'd3-scale';
    import { colours } from '$lib/colours';
    import type { SimpleShotData } from './data/shotData';
    import type { Writable } from 'svelte/store';
    import { key as shotsConcededKey, type LeagueShotsConceded } from './data/leagueShotsConceded';
    import { getContext } from 'svelte';
    import { viewKey, ViewManager } from './view/viewManager';

    let leagueShotsConceded: Writable<LeagueShotsConceded | null> = getContext(shotsConcededKey);
    const viewManager: ViewManager = getContext(viewKey);
    let teamSelected: Writable<string | null> = viewManager.teamSelected;
    
    export let team: Team;
    let shots: SimpleShotData | undefined;
    export let side: ('a' | 'h');
    const xgMin = 0.5;
    const xgMax = 2.5;

    $: shots = $leagueShotsConceded?.data.get(team.title);
    $: xGA = shots == undefined ? 0 : shots.xG / team.games;

    let colourScale = scaleLinear()
        .domain([xgMax, xgMin])
        .range([colours.xg + 'ff', colours.xg + '33']);
    $: colour = $teamSelected != null 
        ? $teamSelected == team.title 
            ? colourScale(xgMax) 
            : colourScale(xgMin)
        : colourScale(xGA);

</script>

<div>
    <div 
        class='inline-block my-1 relative highlight w-full font-normal transition-colors'
        tabindex="-1"
        style='background-color: {colour}; width: {xGA/xgMax * 100}%;'
        on:focus={() => $teamSelected = team.title}
        on:blur={() => {if ($teamSelected == team.title) {$teamSelected = null}}}
    >
        <p>{team.title} ({side.toUpperCase()})</p>
    </div>
    <p class='pb-4 lg:pb-0 lg:inline lg:pl-2 font-normal'>{xGA.toFixed(2)} <span class='text-white-800'>xGA per 90</span></p>
</div>
