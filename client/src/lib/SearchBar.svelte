<script>
    import { onMount } from 'svelte';

    let items = [];
    let searchText = '';
    let prevSearchText = '';
    let filteredItems;
    let selectedIndex = -1;
    let searchEl;
    let linksContainerEl;

    // load
    onMount(async () => {
        fetch('http://localhost:8000/items')
        .then(res => res.json())
        .then(data => {
            items = data;
        })
    });

    // behaviour
    $: filteredItems = items.filter(item => item.name.toLowerCase().includes(searchText.toLowerCase()));
    $: searchText, selectedIndex = -1;

    function handleKeydown(event) {
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
                let links = linksContainerEl.children;
                links[selectedIndex].click();
            }
            else {
                prevSearchText = event.target.value;
            }
        }
    }

    function handleKeyup(event) {
        if (event.key !== 'ArrowUp' && event.key !== 'ArrowDown' && event.target.value !== prevSearchText) {
            searchText = event.target.value;
        }
    }

    function handleWindowKeydown(event) {
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