<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-yellow-500 rounded-lg">
                <h1 class="mb-6 text-2xl">SIGN IN</h1>

                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                </p>

                <p class="font-bold">
                    Don't have an account? <RouterLink to="signup" class="underline">Click here</RouterLink> to Make NEW ONE!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-yellow-500 rounded-lg">
                <form class="space-y-6">

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Password</label><br>
                        <input type="password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>-

                    <div>
                        <button class="py-4 px-6 bg-emerald-600 text-white rounded-lg">LOG IN</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>