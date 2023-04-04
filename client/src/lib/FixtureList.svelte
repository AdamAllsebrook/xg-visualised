<script lang="ts">
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import AveragePointer from './AveragePointer.svelte';
    import { DataManager, key as dataKey } from './data/dataManager';
    import { key as shotsConcededKey, LeagueShotsConceded } from './data/leagueShotsConceded';
    import type { Opponents } from './data/opponents';
    import { SimpleShotData } from './data/shotData';
    import FixtureSummary from './FixtureSummary.svelte';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const opponents: Opponents = $dataManager.opponents;
    const leagueShotsConceded: Writable<LeagueShotsConceded | null> = getContext(shotsConcededKey);
    // this is a constant redefined from another file, probably should fix that... 
    const xgMax = 2.5;

    $: $leagueShotsConceded, console.log($leagueShotsConceded?.data.values());
    $: averageXGA = $leagueShotsConceded == null ? 0 : Array.from($leagueShotsConceded.data.entries()).reduce((a, [team, shots]) => a + shots.xG / $dataManager.teams.get(team).games, 0) / $leagueShotsConceded.data.size;
</script>
<AveragePointer percentage={averageXGA / xgMax * 100} text={`League average ${averageXGA.toFixed(2)} xGA per 90`} />
{#each opponents.teams as team, i}
    <FixtureSummary
        {team}
        side={opponents.sides[i]}
    />
{/each}

