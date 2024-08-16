<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                </p>

                <RouterLink to="/profile/edit/password" class="underline">Edit password</RouterLink>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <h3 class="mb-6 text-xl">friends You May Know</h3>

                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="http://i.pravatar.cc/300?img=20" class="w-[40px] rounded-full">

                            <p class="text-xs"><strong>Live With Your Community</strong></p>
                        </div>
                            <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-leg">show</a>
                    </div>
                    
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="http://i.pravatar.cc/300?img=60" class="w-[40px] rounded-full">

                            <p class="text-xs"><strong>Live With Your Community</strong></p>
                        </div>

                        <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-leg">show</a>
                    </div>
                </div>
            </div>
        
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <h3 class="mb-6 text-xl">Trends</h3>
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <p class="text-xs">
                                <strong>Live With Us</strong><br>
                                <span class="text-gray-500">15000 Posts</span>
                            </p>
                        </div>
                            
                        <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-leg">show</a>
                    </div>
                </div>
            </div> 
        </div>
    </div>
</template>
