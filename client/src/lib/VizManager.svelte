<script lang='ts'>
    import { getContext } from 'svelte';
    import Pitch from '$lib/Pitch.svelte';
    import Matches from '$lib/Matches.svelte';
    import { key, DataManager } from '$lib/data/dataManager';
    import type { Match, Shot } from '$client';
    import type { Margin } from './margin';
    import type { Spring } from 'svelte/motion';

    export let width: number;
    export let height: number;
    export let margin: Margin;
    export let currentStep: number;
    export let tweenedX: Spring<number[]>;
    export let tweenedY: Spring<number[]>;

    const dataManager: DataManager = getContext(key);
    const shots: Shot[] = dataManager.shots;
    const matches: Match[] = dataManager.matches;
</script>


{#if currentStep == undefined || (0 <= currentStep && currentStep <= 4)}
    <Pitch width={width - margin.left - margin.right} height={height - margin.top - margin.bottom} {shots} bind:tweenedX bind:tweenedY/>
{:else if 5 <= currentStep && currentStep <= 7}
    <Matches width={width - margin.left - margin.right} height={height - margin.top - margin.bottom} {matches} {shots}  bind:tweenedX bind:tweenedY/>
{/if}
