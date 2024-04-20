; This is the entry point of our program, it's where the program begins execution
.global _start                        ; Global label, makes _start visible to linker
.intel_syntax noprefix                 ; Use Intel syntax, instead of AT&T syntax

_start:                               ; Label, marks the start of the program
    mov ah, 0x09                       ; Move the value 0x09 into register ah
                                        ; This value represents the BIOS interrupt service routine
                                        ; for printing a string to the console
    mov dx, msg                         ; Move the address of msg into register dx,
                                        ; dx will hold the parameters for the BIOS interrupt service routine
    int 0x21                            ; Call the BIOS interrupt service routine with ah as the function number
                                        ; and dx as the parameters

    mov ah, 0x4c                       ; Move the value 0x4c into register ah, this represents the exit function
                                        ; of the BIOS interrupt service routine
    int 0x21                            ; Call the BIOS interrupt service routine with ah as the function number

section .data                         ; Section declaration, this section will hold initialized data
    msg db 'Hello, World!', 0x0D, 0x0A, '$'  ; db is used to declare a byte array, the array consists of
                                        ; ASCII characters, 0x0D and 0x0A represent the ASCII code for
                                        ; carriage return and line feed respectively, and $ is used to
                                        ; mark the end of the string


                                        