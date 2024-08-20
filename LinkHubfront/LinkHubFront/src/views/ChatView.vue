<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <template>
                                <img src="http://i.pravatar.cc/300?img=10" class="w-[40px] rounded-full">

                                <p >user name</p>
                            </template>
                        </div>

                        <span class="text-xs text-gray-500">last ago</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="flex flex-col flex-grow p-4">
                        <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                            <div>
                                <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                    <p class="text-sm">Hi message body</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">time of message ago</span>
                            </div>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img src="http://i.pravatar.cc/300?img=20" class="w-[40px] rounded-full">

                            </div>
                        </div>

                        <div class="flex w-full mt-2 space-x-3 max-w-md">
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img src="http://i.pravatar.cc/300?img=40" class="w-[40px] rounded-full">

                            </div>
                            <div>
                                <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                                    <p class="text-sm">body of responsing messages</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">time ago</span>
                            </div>
                        </div>
                </div>
            </div>

            <div class="bg-white border border-gray-200 rounded-lg">
                    <div class="p-4">  
                        <textarea class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What do you want to say?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Send</button>
                    </div>
            </div>
        </div>
    </div>
</template>