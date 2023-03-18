<script lang='ts'>
    import type { Shot } from '$client';
    import Circle from '$lib/Circle.svelte';
    import type { HoveredData } from '$lib/hoveredData';
    import ShotTooltip from '$lib/ShotTooltip.svelte';

    export let data: any;
    export let hoveredData: HoveredData | null;
    export let shots: Shot[];
    export let rScale: any;
</script>

{#each data as d, i}
    <Circle
        cx={d.x}
        cy={d.y}
        r={rScale(shots[i].xG)}
        highlight={shots[i].result == 'Goal'}
        faded={hoveredData != null && hoveredData.index != i}
        spotlight={hoveredData != null && hoveredData.index == i}
        on:mouseover={() => {
           hoveredData = {data: shots[i], index: i, component: ShotTooltip};
        }}
        on:focus={() => {
           hoveredData = {data: shots[i], index: i, component: ShotTooltip}
        }}
        on:focusout={() => hoveredData = null}
    />
{/each}
