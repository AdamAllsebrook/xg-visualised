<script lang="ts">
    import { scaleLinear } from 'd3-scale';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import type { Opponents } from '$lib/data/opponents';
    import { SimpleShotData } from '$lib/data/shotData';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import { colours } from '$lib/colours';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const shotData = $dataManager.shotData;

    const minuteBins = SimpleShotData.minuteBins($dataManager.shots);
    const minuteXgs = minuteBins.map((bin) => bin.xG);
    // argmax
    const preferTime = minuteXgs.indexOf(Math.max(...minuteXgs));

    let colourScale = scaleLinear()
        .domain([minuteXgs[preferTime] * 1.5, 0])
        .range([colours.xg + 'ff', colours.xg + '33']);
</script>

<h3 class="font-bold text-2xl">Minutes</h3>
<p class="pb-4">
    {player.player_name} is most likely to score between
    {preferTime * 15} and
    {(preferTime + 1) * 15} minutes, totalling
    <span class="highlight bg-xg">{minuteXgs[preferTime].toFixed(2)} xG</span> in this time period.
</p>
<div class="w-full">
    {#each minuteXgs as xg, i}
        <div
            class="my-1 highlight inline-block"
            style="width: {(xg * 75) / minuteXgs[preferTime]}%; background: {colourScale(xg)};"
        >
            <p class="font-normal whitespace-nowrap">{i * 15} - {(i + 1) * 15} mins</p>
        </div>
        <p class="pb-4 lg:pb-0 inline lg:pl-2 font-normal">
            {xg.toFixed(2)} <span class="text-white-800">xG</span>
        </p>
        <div />
    {/each}
</div>
