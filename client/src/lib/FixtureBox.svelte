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
    const prefersInBox = $dataManager.shotData.insideBox >= $dataManager.shotData.outsideBox;
    
    export let team: Team;
    let shots: SimpleShotData | undefined;
    export let side: ('a' | 'h');

    $: shots = $leagueShotsConceded?.data.get(team.title);
    $: inBox = shots ? shots?.insideBox / shots?.shots: 0;
    $: outBox = shots ? shots?.outsideBox / shots?.shots: 0;

    let colourScale = scaleLinear()
        .domain([0, 1])
        .range([colours.shot + 'ff', colours.shot + '33']);
    $: colour = $teamSelected != null 
        ? $teamSelected == team.title 
            ? colourScale(0) 
            : colourScale(1)
        : colourScale(inBox);

</script>

<div>
    <div 
        class='inline-block my-1 relative highlight w-full font-normal transition-colors'
        tabindex="-1"
        style='background-color: {colour}; width: {(prefersInBox ? inBox : outBox) * 100}%;'
        on:focus={() => $teamSelected = team.title}
        on:blur={() => {if ($teamSelected == team.title) {$teamSelected = null}}}
    >
        <p>{team.title} ({side.toUpperCase()})</p>
    </div>
    <p class='pb-4 lg:pb-0 inline lg:pl-2 font-normal'>{((prefersInBox ? inBox : outBox) * 100).toFixed(2)}% <span class='text-white-800 hidden lg:visible'>of shots conceded</span></p>
</div>
