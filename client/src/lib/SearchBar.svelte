<script lang='ts'>
    import { onMount } from 'svelte';
    import { ItemsService } from '$client';
    import type { PlayerSearch, TeamSearch } from '$client';

    let items: (PlayerSearch | TeamSearch)[]  = [];
    let searchText = '';
    let prevSearchText = '';
    let filteredItems: (PlayerSearch | TeamSearch)[];
    let selectedIndex = -1;
    let searchEl: HTMLInputElement;
    let linksContainerEl: HTMLElement;

    // load
    onMount(async () => {
        ItemsService.itemsRead()
            .then(data => items = data);
    });

    // behaviour
    $: filteredItems = items.filter(item => item.name.toLowerCase().includes(searchText.toLowerCase()));
    $: searchText, selectedIndex = -1;

    function handleKeydown(event: KeyboardEvent) {
        if (searchText.length > 0) {
            if (event.key === 'ArrowUp') {
                selectedIndex -= 1;
                if (selectedIndex < -1) {
                    selectedIndex = filteredItems.length - 1;
                }
                event.preventDefault();
            }
            else if (event.key === 'ArrowDown') {
                selectedIndex += 1;
                if (selectedIndex > filteredItems.length - 1) {
                    selectedIndex = -1;
                }
                event.preventDefault();
            }
            else if (event.key === 'Enter' && selectedIndex > -1) {
                let links = linksContainerEl.querySelectorAll('a');
                links[selectedIndex].click();
            }
            else {
                prevSearchText = searchEl.value;
            }
        }
    }

    function handleKeyup(event: KeyboardEvent) {
        if (event.key !== 'ArrowUp' && event.key !== 'ArrowDown' && searchEl.value !== prevSearchText) {
            searchText = searchEl.value;
        }
    }

    function handleWindowKeydown(event: KeyboardEvent) {
        if (event.key == '/' && event.ctrlKey) {
            searchEl.focus();
        }
    }

</script>

<svelte:window on:keydown={handleWindowKeydown} />

<input 
    type="search" id="search" name="search" placeholder="" autocomplete="off" bind:this={searchEl}
    value={selectedIndex == -1 ? searchText : filteredItems[selectedIndex].name}
    on:keydown={handleKeydown} on:keyup={handleKeyup}
>
<div bind:this={linksContainerEl}>
    {#if searchText.length > 0}
        {#each filteredItems as item, i}
            <a href='/{item.prefix}/{item.id}'>
                <div class:selected="{i == selectedIndex}">{item.name}</div>
            </a>
        {/each}
    {/if}
</div>
<style>
    .selected {
        background-color: antiquewhite;
    }
</style>
