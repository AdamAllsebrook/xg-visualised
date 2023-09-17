<script lang="ts">
    import SearchBar from '$lib/SearchBar.svelte';

    export let data: any;
    const items = data.items;
</script>

<div class="wrapper flex h-[90vh] m-4 text-white-900">
    <div class="container m-auto max-w-2xl">
        <h1 class="font-bold text-5xl font-display text-center pb-16">
            Expected goals, visualised.
        </h1>
        <SearchBar {items} />
        <p class="font-display text-md text-white-800 text-center pt-16">
            <span class="inline-block">An article for every Premier League player,</span>
            <span class="inline-block">
                visualising xG and looking ahead to the next 5 fixtures.</span
            >
        </p>
    </div>
</div>
<div class="text-white-800 font-display fixed bottom-0 w-full flex flex-row items-center">
    <div class="m-auto flex">
        <p class="px-2">by Adam Allsebrook</p>
        <p class="px-2">|</p>
        <a href="https://github.com/AdamAllsebrook/xg-visualised" class="underline px-2">Github</a>
    </div>
</div>
