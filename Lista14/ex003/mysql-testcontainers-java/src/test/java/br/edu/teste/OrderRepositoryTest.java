package br.edu.teste;

import org.junit.jupiter.api.*;
import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import java.math.BigDecimal;
import java.sql.*;

@Testcontainers
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
class OrderRepositoryTest {

    @Container
    static final MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.0")
            .withDatabaseName("app_test")
            .withUsername("testuser")
            .withPassword("testpass")
            .withInitScript("db/schema.sql");

    private static Connection connection;

    @BeforeAll
    static void setup() throws SQLException {
        connection = DriverManager.getConnection(
                mysql.getJdbcUrl(),
                mysql.getUsername(),
                mysql.getPassword()
        );
    }

    @AfterAll
    static void teardown() throws SQLException {
        if (connection != null) {
            connection.close();
        }
    }

    @BeforeEach
    void seedData() throws SQLException {
        try (Statement stmt = connection.createStatement()) {
            stmt.execute("TRUNCATE TABLE orders");
            stmt.execute("""
                INSERT INTO orders (customer_id, total, status)
                VALUES (1, 99.99, 'PENDING')
            """);
        }
    }

    @Test
    @Order(1)
    void deveInserirPedidoERetornarIdGerado() throws SQLException {
        try (PreparedStatement ps = connection.prepareStatement(
                "INSERT INTO orders (customer_id, total, status) VALUES (?, ?, ?)",
                Statement.RETURN_GENERATED_KEYS
        )) {
            ps.setLong(1, 42L);
            ps.setBigDecimal(2, new BigDecimal("149.99"));
            ps.setString(3, "PENDING");

            ps.executeUpdate();

            ResultSet keys = ps.getGeneratedKeys();

            Assertions.assertTrue(keys.next());
            Assertions.assertTrue(keys.getLong(1) > 0);
        }
    }

    @Test
    @Order(2)
    void deveConsultarStatusDoPedido() throws SQLException {
        try (PreparedStatement ps = connection.prepareStatement(
                "SELECT status FROM orders WHERE customer_id = ?"
        )) {
            ps.setLong(1, 1L);

            ResultSet rs = ps.executeQuery();

            Assertions.assertTrue(rs.next());
            Assertions.assertEquals("PENDING", rs.getString("status"));
        }
    }
}