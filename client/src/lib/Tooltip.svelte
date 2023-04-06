<script lang="ts">
    import type { Spring } from 'svelte/motion';
    import type { Shot, Match } from '$client';
	import { fade } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';

    // export let tweenedX: Spring<any>;
    // export let tweenedY: Spring<any>;
    // export let x: number;
    // export let y: number;
    // export let r: number;
    // export let width: number;
    // export let height: number;
    // export let index: number;

    export let limits: any;
    export let x: number;
    export let y: number;
    export let offset: number;

    let selfWidth: number;
    let selfHeight: number;
    let screenWidth: number;
</script>

<svelte:window bind:innerWidth={screenWidth}/>
<div 
    class='fixed bg-[#e5e7ffcc] -translate-x-1/2 transition-all pointer-events-none shadow-lg p-2 rounded-sm whitespace-nowrap text-black z-20' 
    style='top: {y + offset + selfHeight > limits.bottom ? y - selfHeight - offset : y + offset}px;
           left: {screenWidth < 480 ? limits.right / 2 + limits.left : (x + selfWidth / 2 > limits.right ? limits.right - selfWidth / 2 + limits.left : x)}px;'
    bind:clientWidth={selfWidth} 
    bind:clientHeight={selfHeight}
    transition:fade="{{delay: 0, duration: 300, easing: cubicOut}}"
>
    <slot></slot>
</div>
