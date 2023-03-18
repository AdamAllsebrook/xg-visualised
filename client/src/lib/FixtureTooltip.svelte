<script lang="ts">
    import type { Team } from '$client';

    export let data: any;
    export let opponent: Team = data.opponent;
</script>

<p>Average xGA: {(opponent.xGA / opponent.games).toFixed(2)}</p>
