# Contributing to Dashboard Analytics

Thank you for your interest in contributing to Dashboard Analytics!

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the issue tracker
2. If not, create a new issue with:
   - Clear description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment details (OS, Python version, etc.)

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation as needed

4. **Test your changes**
   ```bash
   # Run the application
   python -m uvicorn app.main:app --reload
   
   # Test with demo data
   python scripts/seed_data.py
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Comment complex logic

## Project Structure

When adding new features, maintain the existing structure:

```
app/
├── models/      # Database models
├── services/    # Business logic
├── routers/     # API endpoints
├── templates/   # HTML templates
└── static/      # Static files
```

## Testing

Before submitting:

1. Test all existing functionality
2. Test your new features
3. Check for console errors
4. Verify responsive design on different screen sizes

## Documentation

Update documentation when:

- Adding new features
- Changing existing functionality
- Adding new configuration options
- Creating new data models

## Questions?

Feel free to open an issue for any questions about contributing.

Thank you for helping improve Dashboard Analytics!
