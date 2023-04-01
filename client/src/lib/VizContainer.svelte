<script lang="ts">
    export let width: number;
    export let height: number;
</script>

<div
    class="sticky top-[50%] -translate-y-1/2 lg:float-right"
    style="width: {width}px; height: {height}px"
    on:mouseleave
>
    <slot />
</div>
