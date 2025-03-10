<script lang="ts">
    export let href: string;
    export let style: "normal" | "button" = "normal";
</script>

{#if style == "normal"}
    <a class="font-bold" {href}>
        <slot></slot>
    </a>
{:else if style == "button"}
    <a class="font-bold rounded-full bg-gray-300 p-2 px-4" {href}>
        <slot></slot>
    </a>
{/if}
