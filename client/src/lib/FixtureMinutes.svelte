<script lang="ts">
    import type { SimpleShot, Team } from '$client';
    import { scaleLinear } from 'd3-scale';
    import { colours } from '$lib/colours';
    import { SimpleShotData } from './data/shotData';
    import type { Writable } from 'svelte/store';
    import { key as shotsConcededKey, type LeagueShotsConceded } from './data/leagueShotsConceded';
    import { getContext } from 'svelte';
    import { viewKey, ViewManager } from './view/viewManager';

    let leagueShotsConceded: Writable<LeagueShotsConceded | null> = getContext(shotsConcededKey);
    const viewManager: ViewManager = getContext(viewKey);
    let teamSelected: Writable<string | null> = viewManager.teamSelected;

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
        style="border-color: {colour}; background-color: {$teamSelected == team.title
            ? colour
            : 'transparent'};}"
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
</div>
