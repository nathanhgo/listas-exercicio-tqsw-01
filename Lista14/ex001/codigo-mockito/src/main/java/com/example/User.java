package com.example;
public class User {
    private int id;
    private String username;
    private String email;
    private String firstName;
    private String lastName;

    public User() {}
    public User(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public void setId(int id) { this.id = id; }
    public void setUsername(String username) { this.username = username; }
    public void setEmail(String email) { this.email = email; }
    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        User user = (User) obj;
        return id == user.id && 
               (username != null ? username.equals(user.username) : user.username == null) &&
               (email != null ? email.equals(user.email) : user.email == null);
    }
}
