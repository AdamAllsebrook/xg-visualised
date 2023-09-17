<script lang="ts">
    import { getContext } from 'svelte';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const shots = $dataManager.shotData.shots;
    const goals = $dataManager.goalData.shots;

    const prefersInBox = $dataManager.shotData.insideBox >= $dataManager.shotData.outsideBox;
    const preferredShots = prefersInBox
        ? $dataManager.shotData.insideBox
        : $dataManager.shotData.outsideBox;
    const preferredGoals = prefersInBox
        ? $dataManager.goalData.insideBox
        : $dataManager.goalData.outsideBox;
</script>

<h3 class="font-bold text-2xl">In or Around the Box</h3>
<p>
    {player.player_name} prefers to shoot from
    {prefersInBox ? 'inside' : 'outside'} the box, scoring
    <span class="highlight bg-goal">{preferredGoals} goal{preferredGoals == 1 ? '' : 's'}</span>
    from
    <span class="highlight bg-shot">{preferredShots} shot{preferredShots == 1 ? '' : 's'}</span>,
</p>
<p>
    compared to his
    <span class="highlight bg-goal"
        >{goals - preferredGoals} goal{goals - preferredGoals == 1 ? '' : 's'}</span
    >
    from
    <span class="highlight bg-shot"
        >{shots - preferredShots} shot{shots - preferredShots == 1 ? '' : 's'}
    </span>
    {prefersInBox ? 'outside' : 'inside'} the box.
</p>
