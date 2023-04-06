<script lang='ts'>
    import type { Team } from '$client';
    import { scaleLinear } from 'd3-scale';
    import { colours } from '$lib/colours';
    import type { SimpleShotData } from './data/shotData';
    import type { Writable } from 'svelte/store';
    import { key as shotsConcededKey, type LeagueShotsConceded } from './data/leagueShotsConceded';
    import { getContext } from 'svelte';
    import { viewKey, ViewManager } from './view/viewManager';
    import { DataManager, key as dataKey } from './data/dataManager';

    let leagueShotsConceded: Writable<LeagueShotsConceded | null> = getContext(shotsConcededKey);
    const viewManager: ViewManager = getContext(viewKey);
    let teamSelected: Writable<string | null> = viewManager.teamSelected;


    const dataManager: Writable<DataManager> = getContext(dataKey);
    
    export let team: Team;
    let shots: SimpleShotData | undefined;
    export let side: ('a' | 'h');

    $: shots = $leagueShotsConceded?.data.get(team.title);
    // switch home and away, as a shot is always from pov of shooter, here we want conceded
    $: home = shots ? shots?.xgAway/ shots?.xG: 0;
    $: away = shots ? shots?.xgHome / shots?.xG: 0;

    let colourScale = scaleLinear()
        .domain([0, 1])
        .range([colours.xg + 'ff', colours.xg + '33']);
    $: colour = $teamSelected != null 
        ? $teamSelected == team.title 
            ? colourScale(0) 
            : colourScale(1)
        : colourScale(home);

    $: colour1 = home >= away ? colour : '#fff0';
    $: colour2 = home >= away ? '#fff0' : colour;

</script>

<div class='relative'>
    <div 
        class='inline-block my-1 relative highlight w-full font-normal transition-colors'
        tabindex="-1"
        style='background: linear-gradient(90deg, {colour1} 0%, {colour1} {home * 100}%, {colour2} {home * 100}%, {colour2} 100%);); border: 1px solid {colour}; transition: border-color 0.15s'
        on:focus={() => $teamSelected = team.title}
        on:blur={() => {if ($teamSelected == team.title) {$teamSelected = null}}}
    >
        <p>{team.title} ({side.toUpperCase()})</p>
    </div>
    <div class='flex absolute right-2 lg:right-auto top-2 lg:block lg:relative lg:-translate-y-8'>
        <div class='flex items-center lg:absolute h-full top-0 pr-2 text-white-{home >= away ? 900 : 800} pointer-events-none' style='right: {100 - home * 100}%'>
            <p class=' font-normal' >{(home * 100).toFixed(0)}%</p>
        </div>
        <p class='lg:hidden text-white-800'>/</p>
        <div class='flex items-center lg:absolute h-full top-0 pl-2 text-white-{home >= away ? 800 : 900} pointer-events-none' style='left: {100 - away * 100}%'>
            <p class=' font-normal' >{(away * 100).toFixed(0)}%</p>
        </div>
    </div>
</div>


