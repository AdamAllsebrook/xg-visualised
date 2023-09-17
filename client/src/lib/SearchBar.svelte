<script lang="ts">
    import type { PlayerSearch, TeamSearch } from '$client';
    import { fade } from 'svelte/transition';

    export let items: (PlayerSearch | TeamSearch)[] = [];
    let searchText = '';
    let prevSearchText = '';
    let filteredItems: (PlayerSearch | TeamSearch)[];
    let selectedIndex = -1;
    let searchEl: HTMLInputElement;
    let linksContainerEl: HTMLElement;
    let isFocused = false;

    // behaviour
    $: filteredItems = items
        .filter((item) => normalize(item.name).includes(normalize(searchText)))
        .slice(0, 10);
    $: searchText, (selectedIndex = -1);

    function handleKeydown(event: KeyboardEvent) {
        if (searchText.length > 0) {
            if (event.key === 'ArrowUp') {
                selectedIndex -= 1;
                if (selectedIndex < -1) {
                    selectedIndex = filteredItems.length - 1;
                }
                event.preventDefault();
            } else if (event.key === 'ArrowDown') {
                selectedIndex += 1;
                if (selectedIndex > filteredItems.length - 1) {
                    selectedIndex = -1;
                }
                event.preventDefault();
            } else if (event.key === 'Enter' && selectedIndex > -1) {
                let links = linksContainerEl.querySelectorAll('a');
                links[selectedIndex].click();
            } else {
                prevSearchText = searchEl.value;
            }
        }
    }

    function handleKeyup(event: KeyboardEvent) {
        if (
            event.key !== 'ArrowUp' &&
            event.key !== 'ArrowDown' &&
            searchEl.value !== prevSearchText
        ) {
            searchText = searchEl.value;
        }
    }

    function handleWindowKeydown(event: KeyboardEvent) {
        if (event.key == '/' && event.ctrlKey) {
            searchEl.focus();
        }
    }

    function onFocus() {
        isFocused = true;
    }

    function onBlur() {
        isFocused = false;
    }

    function normalize(text: string) {
        text = text.toLowerCase();
        var from = 'ãàáäâẽèéëêìíïîõòóöôùúüûñç·/_,:;';
        var to = 'aaaaaeeeeeiiiiooooouuuunc------';
        for (let i = 0, l = from.length; i < l; i++) {
            text = text.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
        }
        return text;
    }
</script>

<svelte:window on:keydown={handleWindowKeydown} />

<div class="w-full relative">
    <input
        class="w-full p-4 text-md font-display rounded-sm bg-primary-900 transition-colors
        focus:outline-none focus:bg-primary-800 hover:bg-primary-800 border-b border-primary-700"
        type="search"
        id="search"
        name="search"
        placeholder="Search for a player..."
        autocomplete="off"
        bind:this={searchEl}
        value={selectedIndex == -1 ? searchText : filteredItems[selectedIndex].name}
        on:keydown={handleKeydown}
        on:keyup={handleKeyup}
        on:focus={onFocus}
        on:blur={onBlur}
    />
    {#if searchText.length > 0 && isFocused && filteredItems.length > 0}
        <div
            bind:this={linksContainerEl}
            class="absolute left-0 right-0 text-md py-2 font-display bg-primary-800"
            transition:fade={{ duration: 100 }}
        >
            {#each filteredItems as item, i}
                <a href="/{item.prefix}/{item.id}" class="">
                    <div class="pl-4 p-1" class:bg-primary-700={selectedIndex == i}>
                        {item.name}
                    </div>
                </a>
            {/each}
        </div>
    {/if}
</div>
