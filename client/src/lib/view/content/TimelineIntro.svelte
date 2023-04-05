<script lang='ts'>
    import type { Player } from '$client';
    import { getContext } from 'svelte';
    import { type DataManager, key as dataKey } from '$lib/data/dataManager';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player: Player = $dataManager.player;
</script>

<h3 class='font-bold text-2xl'>Timeline</h3>
<p>
    The timeline shows every shot {player.player_name} has taken this season, organised by the match and minute.
</p>
<p class='text-white-800'>Thinner lines show when he was on the bench.</p>
