<script lang="ts">
    import { fade } from 'svelte/transition';
    import { cubicOut } from 'svelte/easing';

    export let limits: any;
    export let x: number;
    export let y: number;
    export let offset: number;

    let selfWidth: number;
    let selfHeight: number;
    let screenWidth: number;
</script>

<svelte:window bind:innerWidth={screenWidth} />
<div
    class="fixed bg-[#e5e7ffcc] -translate-x-1/2 transition-all pointer-events-none shadow-lg p-2 rounded-sm whitespace-nowrap text-black z-20"
    style="top: {y + offset + selfHeight > limits.bottom ? y - selfHeight - offset : y + offset}px;
           left: {screenWidth < 480
        ? limits.right / 2 + limits.left
        : x + selfWidth / 2 > limits.right
        ? limits.right - selfWidth / 2 + limits.left
        : x}px;"
    bind:clientWidth={selfWidth}
    bind:clientHeight={selfHeight}
    transition:fade={{ delay: 0, duration: 300, easing: cubicOut }}
>
    <slot />
</div>
