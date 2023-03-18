<script lang='ts'>
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import type { Shot } from '$client';
    import Circle from '$lib/Circle.svelte';
    import { type HoveredData, HoveredDataType, key as hoveredDataKey } from '$lib/hoveredData';
    import ShotTooltip from '$lib/ShotTooltip.svelte';

    export let data: any;
    export let shots: Shot[];
    export let rScale: any;

    let hoveredData: Writable<HoveredData | null> = getContext(hoveredDataKey);
</script>

{#each data as d, i}
    <Circle
        cx={d.x}
        cy={d.y}
        r={rScale(shots[i].xG)}
        highlight={shots[i].result == 'Goal'}
        faded={$hoveredData != null && $hoveredData.index != i}
        spotlight={$hoveredData != null && $hoveredData.index == i}
        on:mouseover={() => {
           $hoveredData = {data: shots[i], index: i, component: ShotTooltip, type: HoveredDataType.Shot};
        }}
        on:focus={() => {
           $hoveredData = {data: shots[i], index: i, component: ShotTooltip, type: HoveredDataType.Shot}
        }}
        on:focusout={() => $hoveredData = null}
    />
{/each}
