"""Simple demo to test databricks-connect import without requiring credentials."""

try:
    from databricks.connect import DatabricksSession

    print("✅ databricks-connect imported successfully!")
    print("📦 Module location:", DatabricksSession.__module__)

    # Test that we can create a builder (without connecting)
    builder = DatabricksSession.builder
    print("✅ DatabricksSession.builder created successfully!")

    print("\n🎉 All imports and basic functionality working!")
    print("Next step: Configure your Databricks authentication to connect to a workspace")

except ImportError as e:
    print("❌ Import error:", e)
except Exception as e:
    print("⚠️  Other error:", e)
