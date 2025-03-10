<script lang="ts">
    import { type Summarization } from "$lib/types/summarization";
    import Link from "./link.svelte";
    export let summary: Summarization;
</script>

<div class="rounded-3xl p-6 bg-gray-200">
    <p class="font-bold">In tech:</p>
    <p>
        {summary.summarization}
    </p>
    <p>
        {new Date(summary.timestamp).toLocaleDateString()}
    </p>
    <Link href={summary.link}>Read More</Link>
</div>
