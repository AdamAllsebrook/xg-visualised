<script lang='ts'>
    import Pitch from '$lib/Pitch.svelte';
    import Matches from '$lib/Matches.svelte';

    export let width: number;
    export let height: number;
    export let margin;
    export let currentStep: number;
    export let tweenedX;
    export let tweenedY;
    export let matches;
    export let shots;
</script>


{#if currentStep == 0 || currentStep == undefined}
    <Pitch width={width - margin.left - margin.right} height={height - margin.top - margin.bottom} {shots} bind:tweenedX bind:tweenedY/>
{:else if currentStep == 1}
    <Matches width={width - margin.left - margin.right} height={height - margin.top - margin.bottom} {matches} {shots}  bind:tweenedX bind:tweenedY/>
{/if}
