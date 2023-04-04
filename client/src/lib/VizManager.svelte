<script lang="ts">
    import type { Margin } from './margin';
    import type { Spring } from 'svelte/motion';
    import { viewKey, ViewManager } from './view/viewManager';
    import { getContext } from 'svelte';

    export let width: number;
    export let height: number;
    export let margin: Margin;
    export let rScale: any;
    export let tweenedX: Spring<number[]>;
    export let tweenedY: Spring<number[]>;

    let viewManager: ViewManager = getContext(viewKey);
    let currentStep = viewManager.currentStep;
    let visuals = viewManager.steps.map((step) => step.visuals);
</script>

{#each visuals[$currentStep || 0] as item}
    <svelte:component
        this={item}
        width={width - margin.left - margin.right}
        height={height - margin.top - margin.bottom}
        {rScale}
        bind:tweenedX
        bind:tweenedY
    />
{/each}
