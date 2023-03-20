<script lang='ts'>
    import type { Player } from '$client';

    export let player: Player;
</script>

<h3 class='font-bold text-2xl'>Timeline</h3>
<p>
    This timeline shows every shot {player.player_name} has taken this season, organised by the match and minute.
</p>
