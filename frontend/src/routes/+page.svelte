<script lang="ts">
    import Center from "../components/center.svelte";
    import Page from "../components/page.svelte";
    import Link from "../components/link.svelte";
    import Squeeze from "../components/squeeze.svelte";
    import { TestDatabase, type Database } from "$lib/db";
    import Summary from "../components/summary.svelte";
    import Pill from "../components/pill.svelte";

    const db: Database = new TestDatabase();
</script>

<Page>
    <Center>
        <Squeeze>
            <Center>
                <div class="flex flex-col items-center gap-6">
                    <h1>
                        Your <span class="font-bold">very own</span>
                        personal
                        <i class="font-light">curated</i> news letter
                    </h1>

                    <p>
                        Utilizing <span class="font-bold">the power of AI</span>
                        to bring you the most important news
                        <span class="font-bold"> directly to your inbox</span>.
                    </p>

                    <div class="flex flex-col items-center mb-12">
                        <Link style="button" href="sign-up"
                            >Get Your Daily News Letter &RightArrow;</Link
                        >
                        <p>
                            or <Link href="how-it-works">see how it works</Link>
                        </p>
                    </div>

                    <h2>Choose from our curated news streams</h2>
                    <div class="flex justify-around w-1/2">
                        {#await db.getCategories() then categories}
                            {#each categories as category}
                                <Pill>{category.name}</Pill>
                            {/each}
                        {/await}
                    </div>

                    <h2>Example Summarizations</h2>
                    <div class="flex flex-col justify-between gap-6">
                        {#await db.getLatestSummarizations() then summarizations}
                            {#each summarizations as summary}
                                <Summary {summary} />
                            {/each}
                        {/await}
                    </div>
                </div>
            </Center>
        </Squeeze>
    </Center>
</Page>
