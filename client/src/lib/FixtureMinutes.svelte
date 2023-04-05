<script lang="ts">
    import type { SimpleShot, Team } from '$client';
    import { scaleLinear } from 'd3-scale';
    import { colours } from '$lib/colours';
    import { SimpleShotData } from './data/shotData';
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
    let shots: SimpleShot[] | undefined;
    export let side: 'a' | 'h';

    $: shots = $leagueShotsConceded?.teamShots.get(team.title);
    $: shotData = $leagueShotsConceded?.data.get(team.title);

    $: minuteBins = shots === undefined ? [] : SimpleShotData.minuteBins(shots);
    $: minuteXgs = minuteBins.map((bin) => bin.xG);
    // argmax
    $: preferTime = minuteXgs.indexOf(Math.max(...minuteXgs));

    let colourScale = scaleLinear()
        .domain([0, 1])
        .range([colours.xg + 'ff', colours.xg + '33']);
    $: colour =
        $teamSelected != null
            ? $teamSelected == team.title
                ? colourScale(0)
                : colourScale(1)
            : colourScale(minuteXgs[preferTime] / shotData?.xG ?? 0);
</script>

<div class="relative">
    <div
        class="border lg:w-1/2 my-1 relative highlight w-full font-normal transition-colors"
        style="border-color: {colour}; background-color: {$teamSelected == team.title ? colour : 'transparent'};}"
        tabindex="-1"
        on:focus={() => ($teamSelected = team.title)}
        on:blur={() => {
            if ($teamSelected == team.title) {
                $teamSelected = null;
            }
        }}
    >
        <p>{team.title} ({side.toUpperCase()})</p>
    </div>
    <!-- {#each minuteXgs as xg, i} -->
    <!--     <div -->
    <!--         class="inline-block border text-white-900 pointer-events-none h-8" -->
    <!--         style="width: {shotData === undefined ? 0 : (xg / shotData.xG) * 100}%; border-color: {colour}" -->
    <!--     > -->
            <!-- <p class=" font-normal"> -->
            <!--     {Math.round(shotData === undefined ? 0 : (xg / shotData.xG) * 100)}% -->
            <!-- </p> -->
        <!-- </div> -->
    <!-- {/each} -->
</div>
