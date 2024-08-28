<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <p>We Are LinkHub</p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-grey-500">count friends</p>
                    <p class="text-xs text-grey-500">count posts</p>
                </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="p-4">
                    <textarea class="p-4 w-full bg-gray-100 rounded-leg" placeholder="what are you think about"></textarea>
                </div>

                <div class="bg-white border border-gray-200 rounded-lg">
                    <a href="#" class="inline-block py-4 px-6 bg-blue-600 text-white rounded-leg">Attach Photo Here</a>
                    <a href="#" class="inline-block py-4 px-6 bg-green-400 text-white rounded-leg">Ok Post It</a>
                </div>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="http://i.pravatar.cc/300?img=20" class="w-[40px] rounded-full">

                        <p><strong>LinkHub wiht you</strong></p>
                    </div>

                    <p class="text-gray-600">time minutes ago</p>
                </div>

                <img src="https://unsplash.com/photos/a-stone-building-with-a-clock-tower-in-the-background-bdqdSIi1ICk" class="full rounded-leg">
                
                <div 
                    class="flex space-x-6"
                    v-for="post in posts"
                    v-bind:key="post.id"
                    >
                    hiii hiiiiijj
                </div>
                <div class="flex space-x-6">
                    <div class="flex items-center space-x-6">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                        </svg>

                        <span class="text-gray-500 text-xs">No. of Likes</span>
                    </div>

                    <div class="flex items-center space-x-6">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z" />
                            </svg>


                        <span class="text-gray-500 text-xs">No. of comments</span>
                    </div>
                </div>

                <div class="flex items-center space-x-6">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 5.25 7.5 7.5 7.5-7.5m-15 6 7.5 7.5 7.5-7.5" />
                    </svg>
                </div>
            </div>
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="http://i.pravatar.cc/300?img=20" class="w-[40px] rounded-full">

                        <p><strong>LinkHub wiht you</strong></p>
                    </div>

                    <p class="text-gray-600">time minutes ago</p>
                </div>

                <p>comment from lorumepsum bla blaaaaa</p>
                <div class="flex space-x-6">
                    <div class="flex items-center space-x-6">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                        </svg>

                        <span class="text-gray-500 text-xs">No. of Likes</span>
                    </div>

                    <div class="flex items-center space-x-6">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z" />
                            </svg>


                        <span class="text-gray-500 text-xs">No. of comments</span>
                    </div>
                </div>

                <div class="flex items-center space-x-6">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 5.25 7.5 7.5 7.5-7.5m-15 6 7.5 7.5 7.5-7.5" />
                    </svg>
                </div>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
           <PeopleYouMayKnow/>

           <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'

export default {
    name: 'FeedView',

    components: {
        PeopleYouMayKnow,
        Trends,
    },

    data() {
        return {
            posts: [],
            body: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            axios
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.data
                    console.log('data2', this.posts)
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>
