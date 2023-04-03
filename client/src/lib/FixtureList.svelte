<script lang="ts">
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import { DataManager, key as dataKey } from './data/dataManager';
    import { key as shotsConcededKey, LeagueShotsConceded } from './data/leagueShotsConceded';
    import type { Opponents } from './data/opponents';
    import { SimpleShotData } from './data/shotData';
    import FixtureSummary from './FixtureSummary.svelte';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const opponents: Opponents = $dataManager.opponents;
</script>

{#each opponents.teams as team, i}
    <FixtureSummary
        {team}
        side={opponents.sides[i]}
    />
{/each}

