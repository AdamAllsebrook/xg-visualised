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
    export let index: number;

    let selfWidth: number;
    let selfHeight: number;
    let screenWidth: number;
</script>

<svelte:window bind:innerWidth={screenWidth}/>
<div 
    class='fixed bg-[#e5e7ffcc] -translate-x-1/2 transition-all pointer-events-none shadow-lg p-2 rounded-sm whitespace-nowrap' 
    style='top: {$tweenedY[index] + y + 3*r/2 + selfHeight > height ? $tweenedY[index] + y - selfHeight - 3*r/2 : $tweenedY[index] + y + 3*r/2}px; 
           left: {screenWidth < 480 ? width/2 + x : $tweenedX[index] + x + selfWidth/2 > width ? width - selfWidth/2 : $tweenedX[index] + x}px'
    bind:clientWidth={selfWidth} 
    bind:clientHeight={selfHeight}
    transition:fade="{{delay: 0, duration: 300, easing: cubicOut}}"
>
    <slot></slot>
</div>
