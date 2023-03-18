<script lang="ts">
    import type { Team } from '$client';

    export let data: Team;
</script>

<p>Average xGA: {data.xGA / data.games}</p>
