<script lang="ts">
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import Circle from '$lib/Circle.svelte';
    import ShotTooltip from '$lib/ShotTooltip.svelte';
    import { HoveredDataType } from '$lib/view/hoveredData';
    import { key as dataKey, type DataManager } from './data/dataManager';
    import { viewKey, type ViewManager } from './view/viewManager';

    export let data: any;
    export let rScale: any;
    const dataManager: Writable<DataManager> = getContext(dataKey);
    const shots = $dataManager.shots;

    const viewManager: ViewManager = getContext(viewKey);
    let hoveredData = viewManager.hoveredData;
    const currentStep = viewManager.currentStep;
</script>

{#each data as d, i}
    <Circle
        id={i}
        cx={d.x}
        cy={d.y}
        r={rScale(shots[i].xG)}
        highlight={shots[i].result == 'Goal'}
        faded={($hoveredData != null && $hoveredData.index != i) ||
            (viewManager.steps[$currentStep || 0].shotLayout === 'homeaway' &&
                shots[i].h_a === 'a')}
        spotlight={$hoveredData != null && $hoveredData.index == i}
        on:mouseover={() => {
            $hoveredData = {
                data: shots[i],
                index: i,
                component: ShotTooltip,
                type: HoveredDataType.Shot,
            };
        }}
        on:focus={() => {
            $hoveredData = {
                data: shots[i],
                index: i,
                component: ShotTooltip,
                type: HoveredDataType.Shot,
            };
        }}
        on:focusout={() => ($hoveredData = null)}
    />
{/each}
