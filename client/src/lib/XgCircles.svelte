<script lang='ts'>
    import Circle from '$lib/Circle.svelte';

    export let data;
    export let hoveredData;
    export let shots;
    export let rScale;
</script>

{#each data as d, i}
    <Circle
        cx={d.x}
        cy={d.y}
        r={rScale(shots[i].xG)}
        highlight={shots[i].result == 'Goal'}
        faded={hoveredData != null && hoveredData[1] != i}
        spotlight={hoveredData != null && hoveredData[1] == i}
        on:mouseover={() => {
           hoveredData = [shots[i], i];
        }}
        on:focus={() => {
           hoveredData = [shots[i], i];
        }}
        on:focusout={() => hoveredData = null}
    />
{/each}
