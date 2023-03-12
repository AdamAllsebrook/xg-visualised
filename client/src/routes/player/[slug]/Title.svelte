<script lang='ts'>
    import type { Player } from '$client';
    import { colours } from '$lib/colours';

    export let player: Player;
</script>


<div class='mb-16 relative z-50 lg:w-1/2' style='background-color: {colours.primary}'>
    <h1 class="text-6xl font-display font-bold text-stone-100">{player.player_name}</h1>
    <h2 class="text-md font-display text-stone-300 font-bold">The xG Story</h2>
</div>
