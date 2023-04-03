<script lang='ts'>
    import Pitch from '$lib/Pitch.svelte';
    import Matches from '$lib/Matches.svelte';
    import type { Margin } from './margin';
    import type { Spring } from 'svelte/motion';
    import Heatmap from './Heatmap.svelte';

    export let width: number;
    export let height: number;
    export let margin: Margin;
    export let currentStep: number;
    export let tweenedX: Spring<number[]>;
    export let tweenedY: Spring<number[]>;
</script>



{#if currentStep == 1}
    <Heatmap width={width - margin.left - margin.right} height={height - margin.top - margin.bottom} />
{/if}
{#if currentStep == undefined || (0 <= currentStep && currentStep <= 4)}
    <Pitch width={width - margin.left - margin.right} height={height - margin.top - margin.bottom}  bind:tweenedX bind:tweenedY/>
{:else if 5 <= currentStep && currentStep <= 7}
    <Matches width={width - margin.left - margin.right} height={height - margin.top - margin.bottom} bind:tweenedX bind:tweenedY/>
{/if}
