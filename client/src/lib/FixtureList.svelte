<script lang="ts">
    import type { Fixture, Team } from '$client';
    import FixtureSummary from './FixtureSummary.svelte';
	import type { HoveredData } from './hoveredData';

    export let fixtures: Fixture[];
    export let teams: Map<string, Team>;
    export let hoveredData: HoveredData;
</script>

{#each fixtures as fixture}
    <FixtureSummary
        {fixture}
        {teams}
        bind:hoveredData
    />
{/each}

