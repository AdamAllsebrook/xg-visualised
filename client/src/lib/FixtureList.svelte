<script lang="ts">
    import type { Fixture, Team } from '$client';
    import FixtureSummary from './FixtureSummary.svelte';

    export let fixtures: Fixture[];
    export let teams: Map<string, Team>;
</script>

{#each fixtures as fixture}
    <FixtureSummary
        {fixture}
        {teams}
    />
{/each}

