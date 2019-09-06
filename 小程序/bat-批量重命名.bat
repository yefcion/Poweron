@echo off

set a=00

setlocal EnableDelayedExpansion

for %%n in (*) do (

set /A a+=1

ren "%%n" "pic_!a!.jpg"

)