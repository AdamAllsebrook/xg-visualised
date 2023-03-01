<script lang="ts">
    import type { Spring } from 'svelte/motion';
    import type { Shot, Match } from '$client';
	import { fade } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';

    export let tweenedX: Spring<any>;
    export let tweenedY: Spring<any>;
    export let x: number;
    export let y: number;
    export let r: number;
    export let width: number;
    export let height: number;
    export let shot: Shot | null = null;
    export let match: Match | null = null;
    export let index: number;

    let selfWidth: number;
    let selfHeight: number;
</script>

<div 
    class='fixed bg-[#e5e7ffcc] -translate-x-1/2 transition-all pointer-events-none shadow-lg p-2 rounded-sm whitespace-nowrap' 
    style='top: {$tweenedY[index] + y + 3*r/2 + selfHeight > height ? $tweenedY[index] + y - selfHeight - 3*r/2 : $tweenedY[index] + y + 3*r/2}px; 
           left: {$tweenedX[index] + x + selfWidth/2 > width ? width - selfWidth/2 : $tweenedX[index] + x}px'
    bind:clientWidth={selfWidth} 
    bind:clientHeight={selfHeight}
    transition:fade="{{delay: 0, duration: 300, easing: cubicOut}}"
    >
    {#if shot}
        <p class='font-medium'>{shot.h_team} {shot.h_goals} - {shot.a_goals} {shot.a_team}</p>
        <p class='text-center mb-2 pb-2 border-b-[1px] border-slate-900'>{(new Date(shot.date)).toLocaleDateString()}</p>
        <div class='inline-block pr-2 pl-3 text-right text-slate-900'>
            <p>Minute</p>
            <p>Situation</p>
            <p>Assist</p>
            <p>Shot type</p>
            <p>Result</p>
            <p>xG</p>
        </div>
        <div class='inline-block'>
            <p>{shot.minute}</p>
            <p>{shot.situation.replace(/([A-Z])/g, ' $1').trim()}</p>
            <p>{shot.player_assisted || '-'}</p>
            <p>{shot.shotType.replace(/([A-Z])/g, ' $1').trim()}</p>
            <p>{shot.result.replace(/([A-Z])/g, ' $1').trim().replace('Shots', 'Shot')}</p>
            <p>{shot.xG.toFixed(2)}</p>
        </div>
    {/if}
</div>