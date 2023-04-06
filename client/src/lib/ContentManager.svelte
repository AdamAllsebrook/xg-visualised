<script lang='ts'>
    import { colours } from '$lib/colours';
    import { getContext } from 'svelte';
    import { viewKey, type ViewManager } from './view/viewManager';

    let viewManager: ViewManager = getContext(viewKey);
    let content = viewManager.steps.map((step) => step.content);
    let currentStep = viewManager.currentStep;

</script>

{#each content as item, i}
    <div 
        class='mb-[75vh] lg:mb-[60vh] flex place-items-center justify-center lg:block lg:w-3/5 -translate-y-96 lg:translate-y-32'
        class:active={$currentStep === i}
    >
        <div 
            class='p-8 w-full z-10 text-stone-100 font-display lg:pl-16'
            style='background: linear-gradient(0deg, {colours.primary}33 0%, {colours.primary}ee 20%, {colours.primary}ee 80%, {colours.primary}33 100%)'
        >
        <svelte:component this={item}/>
        </div>
    </div>
{/each}
