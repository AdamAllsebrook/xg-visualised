<script lang="ts">
    import type { Spring } from 'svelte/motion';
    import type { Shot, Match } from '$client';

    export let tweenedX: Spring<any>;
    export let tweenedY: Spring<any>;
    export let x: number;
    export let y: number;
    export let shot: Shot | null = null;
    export let match: Match | null = null;
    export let index: number;
</script>

<div class='fixed bg-white -translate-x-1/2 translate-y-3 transition-all pointer-events-none' style='top: {Math.max(0, $tweenedY[index] + y)}px; left: {Math.max(0, $tweenedX[index] + x)}px'>
    {#if shot}
        <p>{shot.h_team} {shot.h_goals} - {shot.a_goals} {shot.a_team}</p>
        <p class='text-center'>{(new Date(shot.date)).toLocaleDateString()}</p>
        <div class='inline-block pr-1 pl-2 text-right'>
            <p>Minute</p>
            <p>Situation</p>
            <p>Assist</p>
            <p>Shot type</p>
            <p>Result</p>
            <p>xG</p>
        </div>
        <div class='inline-block'>
            <p>{shot.minute}</p>
            <p>{shot.situation}</p>
            <p>{shot.player_assisted}</p>
            <p>{shot.shotType}</p>
            <p>{shot.result}</p>
            <p>{shot.xG.toFixed(2)}</p>
        </div>
    {/if}
</div>