//Contact Management System
#include<stdio.h>
//structure
struct Contact{
    char name[50];
    char email[50];
    char phone[50];
};

//add contacts
void addContacts() {
    FILE *file;
    file= fopen("Contact.txt", "a");

    if(file == NULL) {
        printf("File is not available\n");
    } else {
        struct Contact contact;
        fflush(stdin);
        printf("Enter your name: ");
        fgets(contact.name, sizeof(contact.name), stdin);
        printf("Enter your email address: ");
        fgets(contact.email, sizeof(contact.email), stdin);
        printf("Enter your phone number: ");
        fgets(contact.phone, sizeof(contact.phone), stdin);
        //write the file
        fprintf(file, "%s%s%s\n", contact.name, contact.email, contact.phone);
       
        fclose(file);
        printf("Added to contact management system\n");
    }
}

//display contacts
void displayContacts() {
    FILE *file;
    file= fopen("Contact.txt", "r");

    if(file == NULL) {
        printf("File is not available\n");
    } else {
        struct Contact contact;
        while(fscanf(file, " %[^\n] %[^\n] %[^\n]", contact.name, contact.email, contact.phone) != EOF) { //end of the file
            printf("Name: %s\nEmail: %s\nPhone: %s\n\n", contact.name, contact.email, contact.phone);
        }
        fclose(file);
    }
}

int main() {

    int choice;
    while (choice != 3) {
        printf("Contact Management System: \n");
        printf("1. Add contacts\n");
        printf("2. Display contacts\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
            addContacts();
            break;
            case 2:
            displayContacts();
            break;
            case 3:
            printf("Exiting.....\n");
            break;
            default:
            printf("Invalid\n");
        }
    }
    return 0;
}